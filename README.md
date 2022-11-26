# WEBSTER
A modern tool written in python for hunting open redirection!
Hi everyone! I have written this program with only one aim i.e To increase the chances of getting bugs. Webster is an advanced tool that can fire upto 800+ payload in 3 seconds! Apart from this, Some key features of this tool are:

1. Find Open Redirection on authenticated points: Most of the time, the redirection occurs after authentication. This is where most of the automation tool fails. But fear not! with this tool you can test for open redirection on those authenticated pages by just specifying the cookies. The rest of job will be done by this tool

2. Dynamic Payload Generator: Suppose there is a target that allows only a specific domain to redirect. With this tool, you can just specify the whitelist domain and it will generate special payloads for the whitelist domain in it to bypass open redirection protection

3. Fast: This tool has a tremendous speed! You can test over 800+ payloads within 3-4 seconds.

4. Easy to use: Everyone can use this tool with ease! No programming knowledge is required for it.

5. Customizable: You can use your own payload to increase the probability of getting bugs!

# DEPENDENCIES

1. Colorama

2. Urllib

3. Requests

4. Threading

# FUNCTIONALITY

1. -u: Specify the target url(e.g http://testphp.vulnweb.com)

2. -p: Specify the paylaod file

3. -w: Add a whitelist domain

4. -c: Add cookies(Optional)

5. -t: Speed(Default 100) 

Note: The more you reduce the value of -t, The more faster you'll get output

# Custom Payloads

You can easily add your payloads in the tool. Either open the 'payload.txt' file and add your payload or you can create a completely new file. Please make sure to provide only 'example.com' as your intended domain(The domain where you want the application to redirect should be example.com only)

Note: If your payload contains a whitelist domain (eg bing.com.example.com), then make sure to replace it with %whitelist% (eg: %whitelist%.example.com)
