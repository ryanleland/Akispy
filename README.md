Akispy
======

Light weight python client for Akismet API.

Usage
-----

    c = akispy.Connection('_YOUR_KEY_')
    c.verify_key('example.com')
    
    result = c.comment_check({
        'blog': 'http://yourblogdomainname.com',
        'user_ip': '127.0.0.1',
        'user_agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6',
        'referrer': 'http://www.google.com',
        'permalink': 'http://yourblogdomainname.com/blog/post=1',
        'comment_type': 'comment',
        'comment_author': 'admin',
        'comment_author_email': 'test@test.com',
        'comment_author_url': 'http://www.CheckOutMyCoolSite.com',
        'comment_content': 'It means a lot that you would take the time to review our software.  Thanks again.'
    })