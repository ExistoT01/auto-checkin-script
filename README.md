# 接龙管家，晚点名，自动提交脚本

可以实现「接龙管家」的自动接龙上报，上报成功或失败后发送上报状态邮件到本人账号

**注意：仅供学习交流之用，请勿用作商业用途**

**局限：后端 `authorization`(JWT令牌) 有效期只有三天，所以需要三天重新微信扫描获取新的 `authorization`，因此此脚本使用有一定的局限性**

## 实现思路

模拟发起请求，代入相应线程的`data`及`authorization`数据，最后向本人邮箱发送邮件即可(如果只为接龙，此功能可忽略)

## 使用方法

1. 获取线程`data`及`authorization`数据

   - 浏览器打开网页版[接龙管家](https://i.jielong.co/)，打开相应的接龙项目，`F12`打开开发者界面

   ![image-20220512094021528](https://expicture.oss-cn-beijing.aliyuncs.com/img/202205121001173.png)

   - `F5`刷新页面，在`Fetch/XHR`中找到`GetCurrentUser`文件

   ![image-20220512094207661](https://expicture.oss-cn-beijing.aliyuncs.com/img/202205121001175.png)

   - 在`Headers`中获取`Authorization`，记录下来

   ![image-20220512094324252](https://expicture.oss-cn-beijing.aliyuncs.com/img/202205121001176.png)

   - 先进行一次手动填报

   ![image-20220512094512242](https://expicture.oss-cn-beijing.aliyuncs.com/img/202205121001177.png)

   - 找到`EditCheckInRecord`文件，在`Payload`页面的数据就是我们需要更改的`data`数据
     - **注意：如果上报表单中有录音/签名/位置/拍照项，是不支持网页请求打卡的，需要用小程序端打卡，但是「只要录音/签名/位置/拍照项不是必要项，你依然可以使用网页请求打卡」**
     - 至于修改哪些数据，检查你接龙项目的必要项，比如署名对应`Signature`，序号对应`Number`，一些填报选项在`RecordValues`里，按需更改即可

   ![image-20220512094826336](https://expicture.oss-cn-beijing.aliyuncs.com/img/202205121001178.png)

2. 在`check-in.py`文件中修改响应数据即可

   ![image-20220512095927082](https://expicture.oss-cn-beijing.aliyuncs.com/img/202205121001179.png)

3. 将脚本部署到服务器，定点执行，即可自动完成每日打卡
