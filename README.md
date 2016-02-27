# Simple Whatsapp Bots

To run, follow these steps on command line:
 - Install yowsup libraries using pip: ```pip install yowsup2```

 - Register on Whatsapp using OTP method. In the below commands, replace 91 with your country code and 917838xxxx8
 with your phone number prepended with the country code. Example, if phone number is 7838xxxx8 and country code is 91, then:

 ```yowsup-cli registration --requestcode sms --phone 917838xxxxx8 --cc 91```

 - You will receive an OTP, authenticate it using the below command where 123456 is the OTP you received.
  ```yowsup-cli registration --register 123456 --phone 917838xxxxx8 --cc 91```

 - The above step will return a password. Note it down.
 - Add your phone number and password received above in ```config.py``` file.

Make sure Yowsup is in your PYTHONPATH. Then run the application using :

```python run.py```

Now you can chat with this echobot by sending it whatsapp messages from any other number.

So far, I've just replicated the echo-bot described in Yowsup's tutorials. Will try to add more soon.

Shoot me a tweet on [@_ioctl](https://twitter.com/_ioctl) in case you need me. Also Checkout
[yowsup's repository](https://github.com/tgalal/yowsup) for setup related help: