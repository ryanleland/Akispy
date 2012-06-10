#!/usr/bin/env python

"""Light weight python client for Akismet API."""

__title__ = 'akispy'
__version__ = '0.1'
__author__ = 'Ryan Leland'
__copyright__ = 'Copyright 2012 Ryan Leland'

import httplib, urllib

class Akispy(object):
    _key     = None
    _version = None
    _conn    = None
    
    def __init__(self, api_key, version="1.1", service_url="rest.akismet.com"):
        """Akispy class constructor.
        
        API key can be acquired from http://akismet.com/.
        """
    
        self._key = str(api_key)
        self._version = version
        
        # Get connection
        self._conn = httplib.HTTPConnection('%s.%s' % (self._key, service_url))
        
    def verify_key(self, url):
        """For verifying your API key.
        
        Provide the URL of your site or blog you will be checking spam from.
        """
        
        response = self._request('submit-spam', {
            'blog': url,
            'key': self._key
        })
        
        if response.status is 200:
            # Read response (trimmed of whitespace)
            return response.read().strip() is "valid"
            
        return False
        
    def comment_check(self, params):
        """For checking comments."""
    
        # Check required params for comment-check
        for required in ['blog', 'user_ip', 'user_agent']:
            if required not in params:
                raise MissingParams(required) 
    
        response = self._request('comment-check', params)
        
        if response.status is 200:
            # Read response (trimmed of whitespace)
            return response.read().strip() is "true"
            
        return False
        
    def submit_spam(self, params):
        """For submitting a spam comment to Akismet."""
    
        # Check required params for submit-spam
        for required in ['blog', 'user_ip', 'user_agent']:
            if required not in params:
                raise MissingParams(required) 
    
        response = self._request('submit-spam', params)
        
        if response.status is 200:
            return response.read() is "true"
            
        return False
        
    def submit_ham(self, params):
        """For submitting a ham comment to Akismet."""
    
        # Check required params for submit-ham
        for required in ['blog', 'user_ip', 'user_agent']:
            if required not in params:
                raise MissingParams(required) 
    
        response = self._request('submit-ham', params)
        
        if response.status is 200:
            return response.read() is "true"
            
        return False
        
    def _request(self, function, params, method='POST', headers={}):
        """Builds a request object."""
        
        if method is 'POST':
            params = urllib.urlencode(params)
            headers = { "Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain" }
        
        path = '/%s/%s' % (self._version, function)
        
        self._conn.request(method, path, params, headers)
        return self._conn.getresponse()
        
class MissingParam(Exception):
    """Thrown if a required Akismet API method param is missing."""