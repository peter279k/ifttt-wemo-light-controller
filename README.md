# IFTTT WeMo Light Controller

![IFTTT WeMo Light Controller Architecture](https://i.imgur.com/NMQCFKj.png)

## Usage

- Clone the repository with `gi clonet` command.
- Ensure the `Python 3` is available on your running host.
- Adding the Cronjob to send the request every minute to the specific IFTTT maker service URL and check whether your WeMo light should trurn on or off.
- The sample Cronjob setting is as follows:

```
# m h  dom mon dow   command
* * * * * cd /root/ifttt-wemo-light-controller && export TZ=Asia/Taipei && python3 light_controller.py
```
