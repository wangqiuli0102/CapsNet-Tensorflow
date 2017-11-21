# CapsNet-Tensorflow

[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=plastic)](CONTRIBUTING.md)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=plastic)](https://opensource.org/licenses/Apache-2.0)
![completion](https://img.shields.io/badge/completion%20state-90%25-blue.svg?style=plastic)
[![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg?style=plastic)](https://gitter.im/CapsNet-Tensorflow/Lobby)

A Tensorflow implementation of CapsNet based on Geoffrey Hinton's paper [Dynamic Routing Between Capsules](https://arxiv.org/abs/1710.09829)

![capsVSneuron](imgs/capsuleVSneuron.png)

> **Status:**
> 1. The capsule of MNIST version is finished. The current `test accuracy =  99.57`, see details in the `Results` section

> **Daily task**
> 1. multi-GPU support
> 2. Improving the reusability of ``capsLayer.py``, what you need is ``import capsLayer.fully_connected`` or ``import capsLayer.conv2d`` in your code

> **Others**
> 1. [Here(知乎)](https://zhihu.com/question/67287444/answer/251460831) is an answer explaining my understanding of the paper. It may be helpful in understanding the code.
> 2. If you find out any problems, please let me know. I will try my best to 'kill' it ASAP.


## Requirements
- Python
- NumPy
- [Tensorflow](https://github.com/tensorflow/tensorflow) (I'm using 1.3.0, not yet tested for older version)
- tqdm (for displaying training progress info)
- scipy (for saving images)

## Usage
**Step 1.** 
Clone this repository with ``git``.

```
$ git clone https://github.com/naturomics/CapsNet-Tensorflow.git
$ cd CapsNet-Tensorflow
```

**Step 2.** 
Download the [MNIST dataset](http://yann.lecun.com/exdb/mnist/), ``mv`` and extract it into ``data/mnist`` directory.(Be careful the backslash appeared around the curly braces when you copy the ``wget `` command to your terminal, remove it)

```
$ mkdir -p data/mnist
$ wget -c -P data/mnist http://yann.lecun.com/exdb/mnist/{train-images-idx3-ubyte.gz,train-labels-idx1-ubyte.gz,t10k-images-idx3-ubyte.gz,t10k-labels-idx1-ubyte.gz}
$ gunzip data/mnist/*.gz
```

**Step 3.** 
Start the training:
```
$ pip install tqdm  # install it if you haven't installed yet
$ python main.py
```

> The default parameters of batch size is 128, and epoch is 50. You may need to modify the ``config.py`` file or use command line parameters to suit your case. In my case, I run ``python main.py  --test_sum_freq=200 --batch_size=48`` for my 4G GPU(~10min/epoch)

## Results

- training loss

![total_loss](results/total_loss.png)
![margin_loss](results/margin_loss.png)
![reconstruction_loss](results/reconstruction_loss.png)

- test accuracy(using reconstruction)

Routing iteration | 1 | 2 | 3 |
:-----|:----:|:----:|:------|
Test accuracy | 0.43 | 0.44 | 0.49 |
*Paper* | 0.29 | - | 0.25 |

![test_acc](results/routing_trials.png)


> My simple comments for capsule
> 1. A new version neural unit(vector in vector out, not scalar in scalar out)
> 2. The routing algorithm is similar to attention mechanism
> 3. Anyway, a great potential work, a lot to be built upon

------------
### TODO:
- Finish the MNIST version of capsNet (progress:90%)
- Do some different experiments for capsNet:
  * Try Using other datasets
  * Adjusting the model structure
 
- There is [another new paper](https://openreview.net/pdf?id=HJWLfGWRb) about capsules(submitted to ICLR 2018), a follow-up of the CapsNet paper.

## My weChat:
 ![my_wechat](/imgs/my_wechat_QR.png)

### Reference
- [XifengGuo/CapsNet-Keras](https://github.com/XifengGuo/CapsNet-Keras): referred for code optimization
