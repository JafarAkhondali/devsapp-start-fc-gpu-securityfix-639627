
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ${模版名称}` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# fc3-http-gpu-inference-modelscope-cv-ofa-visual-grounding-refcoco 帮助文档
<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc3-http-gpu-inference-modelscope-cv-ofa-visual-grounding-refcoco&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=fc3-http-gpu-inference-modelscope-cv-ofa-visual-grounding-refcoco" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc3-http-gpu-inference-modelscope-cv-ofa-visual-grounding-refcoco&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=fc3-http-gpu-inference-modelscope-cv-ofa-visual-grounding-refcoco" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc3-http-gpu-inference-modelscope-cv-ofa-visual-grounding-refcoco&type=packageDownload">
  </a>
</p>

<description>

快速部署 ModelScope OFA Visual Grounding Large-EN 推理模型至FC-GPU运行环境(fc3.0)

</description>

<codeUrl>

- [:smiley_cat: 代码](https://github.com/devsapp/start-fc-gpu)

</codeUrl>
<preview>

- [:eyes: 预览](http://www.devsapp.cn/details.html?name=fc3-http-gpu-inference-modelscope-cv-ofa-visual-grounding-refcoco)

</preview>


## 前期准备

使用该项目，您需要有开通以下服务并拥有对应权限：

<service>



| 服务/业务 |  权限  | 相关文档 |
| --- |  --- | --- |
| 函数计算 |  创建函数 | [帮助文档](https://help.aliyun.com/product/2508973.html) [计费文档](https://help.aliyun.com/document_detail/2512928.html) |

</service>

<remark>



</remark>

<disclaimers>

免责声明：   
本项目仅用于相关框架与功能的使用示例，不承担额外的使用风险。

</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=fc3-http-gpu-inference-modelscope-cv-ofa-visual-grounding-refcoco) ，
  [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=fc3-http-gpu-inference-modelscope-cv-ofa-visual-grounding-refcoco) 该应用。
   
</appcenter>
<deploy>
    
- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://docs.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init fc3-http-gpu-inference-modelscope-cv-ofa-visual-grounding-refcoco -d fc3-http-gpu-inference-modelscope-cv-ofa-visual-grounding-refcoco`
  - 进入项目，并进行项目部署：`cd fc3-http-gpu-inference-modelscope-cv-ofa-visual-grounding-refcoco && s deploy -y`
   
</deploy>

## 案例介绍

<appdetail id="flushContent">

- OFA(One-For-All)是通用多模态预训练模型，使用简单的序列到序列的学习框架统一模态（跨模态、视觉、语言等模态）和任务（如图片生成、视觉定位、图片描述、图片分类、文本生成等），详见ICML 2022 OFA论文：https://arxiv.org/abs/2202.03052
- 本应用模板基于OFA模型实现了图像语义与视觉定位，预训练数据集为Refcoco。

| input | text | output |
|  ----  | ---- | ----  |
| ![图片alt](https://github.com/devsapp/start-fc-gpu/blob/main/materials/visual_grounding.png?raw=true) | "a blue turtle-like pokemon with round head"  | ![图片alt](https://github.com/devsapp/start-fc-gpu/blob/main/materials/visual_grounding_result1.png?raw=true) |
| ![图片alt](https://github.com/devsapp/start-fc-gpu/blob/main/materials/suitcases.png?raw=true) | "a white suitcases"  | ![图片alt](https://github.com/devsapp/start-fc-gpu/blob/main/materials/suitcases_result1.png?raw=true) |
| ![图片alt](https://github.com/devsapp/start-fc-gpu/blob/main/materials/suitcases.png?raw=true) | "a green suitcases"  | ![图片alt](https://github.com/devsapp/start-fc-gpu/blob/main/materials/suitcases_result2.png?raw=true) |

- 容器环境说明

|  env   |  value  |
|  ----  | ----  |
| Container OS | Ubuntu 20.04 |
| CUDA  | 11.8.0 |
| cuBLAS  | 11.11.3.6 |
| cuDNN   | 8.6.0.163 |
| cuTENSOR  | 1.6.1.5 |
| PyTorch | 1.13.0a0+936e930 |

</appdetail>

## 使用流程

<usedetail id="flushContent">

## 通过应用中心部署

通过应用中心部署完函数之后，可以在应用的具体环境页面，查看到应用的函数资源：

![](http://image.editor.devsapp.cn/evBw7lh8ktv6xDBzSSzvjr1ykchAF9hG41gf1ek1sk8tr4355A/FZa954tvfbe42G9j2qkw.png)

通过函数资源对应的函数链接，可以查看到函数的endpoint地址：

![](http://image.editor.devsapp.cn/evBw7lh8ktv6xDBzSSzvjr1ykchAF9hG41gf1ek1sk8tr4355A/cgzyhg9aFae5avCrrryd.png)


根据此地址，可以进行函数的调用等操作，测试脚本为：

```python
# test.py
import sys
import requests

def main(url, path, text):
    image = open(path, "rb").read()
    params = {"text": text}
    resp = requests.post(url,
                         data = image,
                         headers = {'Content-Type': 'application/octet-stream'},
                         params = params)
    open("output.png", "wb").write(resp.content)
    print("infernece ok, please check output.png")


if __name__ == "__main__":
    # eg1: python3 ./test/client.py http://127.0.0.1:9000/invoke ./test/imgs/visual_grounding.png "a blue turtle-like pokemon with round head"
    # eg2: python3 ./test/client.py http://127.0.0.1:9000/invoke ./test/imgs/suitcases.png "a white suitcases"
    # eg3: python3 ./test/client.py http://127.0.0.1:9000/invoke ./test/imgs/suitcases.png "a green suitcases"

    if len(sys.argv) != 4:
        sys.exit("Usage: client.py <request url> <image path> <query text>")
    main(sys.argv[1], sys.argv[2], sys.argv[3])

```

可以通过执行命令进行测试：

- ```python3 ./test/client.py http://{your_function_http_endpoint}/invoke ./test/imgs/visual_grounding.png "a blue turtle-like pokemon with round head"```    

- ```python3 ./test/client.py http://{your_function_http_endpoint}/invoke ./test/imgs/suitcases.png "a white suitcases"```

- ```python3 ./test/client.py http://{your_function_http_endpoint}/invoke ./test/imgs/suitcases.png "a green suitcases```

</usedetail>

## 注意事项

<matters id="flushContent">
</matters>


<devgroup>


## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">  

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <center>微信公众号：`serverless`</center>                                                                                         | <center>微信小助手：`xiaojiangwh`</center>                                                                                        | <center>钉钉交流群：`33947367`</center>                                                                                           |
</p>
</devgroup>
