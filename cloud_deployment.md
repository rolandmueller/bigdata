# Cloud Deployment


In the Docker exercise, you could open your solution on your laptop by entering in your brower the address http://localhost:4000 or http://127.0.0.1:4000. localhost and 127.0.0.1 will point to your own laptop and listen to the port 4000. This is fine for development. However, at some point you want to share your solution with other people. This is the goal of cloud deployment. Instead of a URL like http://localhost:4000 that only is accessable on your machine, you want an URL like http://www.example.com that works everywhere. The local Docker container must be somehow deployed to a cloud server. How do we get a local Docker image to the cloud?

There are many ways to deploy a Docker container. We will just discuss one example: [Caprover](https://caprover.com/). CapRover helps deploying Docker containers to a Virtual Private Server (VPS).

You as a developer want to give the end user a URL (Uniform Resource Locator, that means a web adress), so the he or she can e.g. interacte with your nice web dashboard or use your API (Application Programming Interface). 

If a user types in in your URL (e.g. www.example.com), the browser will look up in the Domain Name System (DNS) its Internet Protocol (IP) address. So DNS translates the URL (e.g. www.hwr-berlin.de) to a IP address (e.g. 194.94.22.19). If you copy 194.94.22.19 in the browser, you would also land at the web server of the HWR Berlin. However, the IP number is much harder to remember. The IP address is kind of the address of the server. If you create your own cloud server, this server would have an IP address, with which you can reach it.

 The following diagram shows how CapRover works.

![Caprover](https://caprover.com/img/captain-architecture.png)

CapRover will run one or more Docker container for you and will allow you to manage and monitor them on one server. That means on one server you can run multiple projects, each with its own Docker image and its own URL. CapRover itself also runs as a Docker container on your server.

A web browser would use a URL and then the IP address and a port to interact with your server. Port 80 is the standard for non-encripted HTTP (Hypertext Transfer Protocol) traffic. If it is encripted, that means it is secure, then it would use Hypertext transfer protocol secure (HTTPS) on part 443. For using HTTPS you need a digital certificate. However, [Let's Encrypt](https://en.wikipedia.org/wiki/Let%27s_Encrypt) will provide you one for free. CapRover will automatically communicate with Let's Encrypt to get a digital certificate for you, so it is very easy to have https URL.

[Nginx](https://en.wikipedia.org/wiki/Nginx) is a web server, that acts as an [reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy). Nginx will map an incoming call from a web browser to the right Docker container. You can map different URLs to different Docker containers. That means, you can point multiple URLs to the same IP address (the same server), but depending on the URL, Nginx will forward the traffic to the right Docker container. With CapRover you can manage this mapping of Nginx and the Docker containers. 

CapRover helps you to deploy the Docker containers as a developer. It has a Command Line Interface (CLI) to deploy your code to the server with just one command (`caprover deploy`). It has also a web interface to access, manage, and monitor your server. Also there are many one-click apps (like Wordpress) available, that you can deploy in the web interface without any coding.

To be able to deploy to a CapRover server, you need the following things:

1. A cloud server (Virtual Private Server, VPS). 

    You can get them, e.g. from [Hetzner](https://www.hetzner.com/cloud) or [Digitalocean](https://www.digitalocean.com/products/droplets) or from any of the cloud hyperscalers (e.g., AWS, Azure, Google Cloud). There is also a quite generous [free tier from Oracle](https://www.oracle.com/cloud/free/) that you might want to check out. Hetzner is a German cloud provider with very competitive pricing. If you get the GitHub Student Developer Pack, you get a Digitalocean $200 credit for 60 days. However, Hetzner has better prices than Digitalocean. GitHub Student Developer Pack also includes $100 Microsoft Azure credit.  
    
    [Hetzner](https://docs.hetzner.com/cloud/apps/list/docker-ce/) and [Digitalocean](https://marketplace.digitalocean.com/apps/docker) offer Docker CE apps, that means servers, where Docker is already pre-installed. When you create a VPS, you should select the Docker CE app, so that you do not have to install Docker on the server by yourself. If you have a VPS without preinstalled Docker, you can follow the installation instruction on the Docker website, e.g. for [installing Docker on a Ubuntu Server](https://docs.docker.com/engine/install/ubuntu/). Digitalocean has even a [CapRover app](https://marketplace.digitalocean.com/apps/caprover). After creating a VPS, write down the IP address and the root password of your VPS.

2. A domain name

    You can get a .com or a .de domain from e.g. [Namecheap](https://www.namecheap.com/) for ~ 7€ to 10€ per year. There are other top-level domains (TLD) that might be cheaper or more expensive, and there might be some special deals (e.g., for students or for the first year). However, it might be a good strategy to have your own domain name for the long term, to show some projects to potential employers. 

3. Add a Wild Card entry at your Domain Name register

    https://caprover.com/docs/get-started.html#step-2-connect-root-domain

    Add a wildcard DNS entry for your VPS at your Domain Name register (e.g. namecheap.com).

    Go to the domain name panel of your Domain Name register and add an *A Record*:
    * Host should be a wild card for a subdomain, e.g. `*.dev`
    * Value (Points to) should be the IP Address of your VPS

    Go to https://mxtoolbox.com/DNSLookup.aspx and check if you enter your URL, i.e. randomthing123.dev.mydomain.com (change mydomain.com to your domain), it resolves to your IP address. DNS propagation might take some time, so the domain might not be available immidiately. 

4. Install CapRover on the server

    Log into your VPS with ssh. In the terminal, enter (change 123.123.123.123 to the IP-Address of your VPS):

    ```bash
    ssh root@123.123.123.123
    ```
    
    Configure the firewall on the server:
    https://caprover.com/docs/firewall.html . Run on the server:
    ```bash
    ufw allow 80,443,3000,996,7946,4789,2377/tcp; ufw allow 7946,4789,2377/udp;
    ```

    Install CapRover on the server:
    If you use a VPS app (droplet) with pre-installed Docker, go ahead and install CapRover (if not, you have to [first install Docker on the server ](https://docs.docker.com/engine/install/ubuntu/.)):
    https://caprover.com/docs/get-started.html#step-1-caprover-installation Run on the server:

    ```bash
    docker run -p 80:80 -p 443:443 -p 3000:3000 -v /var/run/docker.sock:/var/run/docker.sock -v /captain:/captain caprover/caprover
    ```

    Once install, go to http://[IP_OF_YOUR_SERVER]:3000 and login with the password `captain42`

    This [CapRover tutorial](https://caprover.com/docs/get-started.html) might help if you are stuck.
    
    If you use Hetzner and you used the Docker CE App, you can use [this tutorial](https://community.hetzner.com/tutorials/install-caprover) and skip step 1.

    [This](https://www.youtube.com/watch?v=VPHEXPfsvyQ) and [this YouTube videos](https://www.youtube.com/watch?v=E16KymP6284) are also good tutorials for the installation.

4. Install the CapRover CLI on you Laptop

    With the CapRover CLI (Command Line Interface) you can type in your terminal on your laptop `caprover deploy` and your local project will deployed to your server. 

    Before installing the CapRover CLI, you have to install Node.js. Just dowload the installer and follow this instruction: https://kinsta.com/blog/how-to-install-node-js/

    Then continue with installing the CapRover CLI: https://caprover.com/docs/get-started.html#step-3-install-caprover-cli 

    Installing CapRover CLI. Run on your laptop:
    ```bash
    npm install -g caprover
    ```

    Configure the CapRover server. Run on your laptop:
    ```bash
    caprover serversetup
    ```

5. Deploy the Docker example from the last exercise.

    The Docker example had two components:
    
    1. The Redis Database

    You can install Redis as a one-click app in the web gui of your CapRover. 
    
    If you go the redis app, you can see that the internal name of the app is `srv-captain--redis`. Through this name other Docker containers on the CapRover server can use this Redis database.

    Under the side menu `Apps`, click on the button `One Click-Apps / Databases` and search for Redis. Name the app `redis`. Add in the password field the same password from the Docker exercise (e.g. `MyBIPMPassword`). 

    2. Your Flask Web app

    On your web GUI of your CapRover, create a new app with the name `flask` (entering in the field). You do NOT need Persistent Data. The counter data is stored in the Redis database.

    Click on the created `flask` and click on the `App Configs` tab. In the Environmental Variables, click `Add Key/Value Pair`: 
    Key:  REDIS_PASSWORD
    Value: MyBIPMPassword (or your password)

    Add another `Add Key/Value Pair`:
    Key:  REDIS_HOST
    Value: srv-captain--redis

    Click on `Save & Update`

    Create a new file in the docker folder with the name `captain-definition` with the [following content](https://caprover.com/docs/captain-definition-file.html#use-dockerfile-in-captain-definition):
    ```json
    {
        "schemaVersion": 2,
        "dockerfilePath": "./Dockerfile"
    }
    ```

    Add `captain-definition` to Git. Commit and push.

    Enter in the laptop in the docker folder in the terminal
    ```bash
    caprover login
    ```

    Now we can use the [CapRover CLI](https://caprover.com/docs/cli-commands.html) to deploy the app.

    Enter in the terminal 
    ```bash
    caprover deploy
    ```

    and select the information of your server and deploy to the flask app.

    On the CapRover web GUI you can find the public URL, under "Your app is publicly available at:"

    Click on the link to see how it looks.

    If you change the code and want to deploy again. To use the previously-entered values for the current directory, without being asked again, use the -d option:
    ```bash
    caprover deploy -d
    ```

7. Create at your domain provider (e.g. Namecheap) a new subdomain (like `counter` (without a wild card (star) before)) and point it to the same IP-address of your VPS. In the CapRover Web GUI for the flask app, add the full domain (e.g. counter.example.com) and clock on `Connect New Domain`. Test if you can reach your app also to the new app (e.g. at http://counter.example.com).

8. In the CapRover Web GUI for the newly added domain (e.g. at http://counter.example.com), click `Enable HTTPS`. Test if you can reach your app with the https URL (e.g. at https://counter.example.com).

9. In the CapRover Web GUI, enable `Force HTTPS by redirecting all HTTP traffic to HTTPS`. Enter your domain without https (e.g. at http://counter.example.com) and test if you get redirected to the https URL (e.g. to https://counter.example.com).

# Deliverables

* Add your URL of the deployed web app in the Moodle
