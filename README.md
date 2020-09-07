# ✊Rock_✋Paper_✌Scissors

## Table of Contents

- [📘 Description](#-description)
- [🏃‍♂️ Getting Started](#-getting-started)
  * [👨🏻‍🏫  Prerequisites](#--prerequisites)
  * [🔧 How to Install](#--how-to-install)
- [Built With ❤️](#-built-with)
- [💁🏻 Contributing](#-contributing)
- [License](#license)



## 📘 Description



## 🏃‍♂️ Getting Started


### 👨🏻‍🏫  Prerequisites

To install all the dependencies, run:

``` pip install --user -r requirements.txt ```


### 🔧 How to Install

1.👯 Clone the Repository:
```sh
$ git clone https://github.com/Harikrishnan6336/Rock_Paper_Scissors.git 
```

2. Then move to the working directory.

3. Collect images for each label (rock, paper and scissors and none):
In this example, we gather 200 images for the "rock" gesture similarly do for paper,scissors and none
```sh
$ python3 collect_images.py <label_name> <num_samples> 
```
For example
```sh
$ python3 collect_images.py paper 200 
```

4. Train the model
```sh
$ python3 train.py 
```

5. Play the game ✨
```sh
$ python3 main.py
```


## Built With ❤️ 

* [Python3.6](https://docs.python.org/3.6/) - ⚠️️ Warning : Tensorflow is not supported on any version of python above 3.6 as of now.
* [Tensorflow](https://www.tensorflow.org/) - The deep learning framework used
* [OpenCV4](https://opencv.org/) - A library of programming functions mainly used for real-time computer vision
* [SqueezeNet](https://github.com/rcmalli/keras-squeezenet) - A deep neural network for computer vision 


## 💁🏻 Contributing


Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. 🍴 Fork the Project
2. Create your Feature Branch (`git checkout -b feature/newFeature`)
3. Commit your Changes (`git commit -m 'Add some newFeature'`)
4. Push to the Branch (`git push origin feature/newFeature`)
5. Open a Pull Request

Please feel free to raise any issue...

## Contributors
[![Contributors][contributors-shield]][contributors-url]

- [Nandakishor M Pai](https://github.com/nandakishormpai2001)

- [Hari Krishnan U](https://github.com/Harikrishnan6336)


## License
[![MIT License][license-shield]][license-url]

Distributed under the MIT License. See `LICENSE` for more information.

[license-shield]: https://img.shields.io/github/contributors/Toshiuk/r5go-b2w-front.svg?style=flat-square
[license-url]: https://github.com/Harikrishnan6336/Rock_Paper_Scissors/blob/master/LICENSE
[contributors-shield]: https://img.shields.io/github/contributors/Harikrishnan6336/Rock_Paper_Scissors
[contributors-url]: https://github.com/Harikrishnan6336/Rock_Paper_Scissors/graphs/contributors
