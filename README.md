<h1 align="center">Getting Comments From Hepsiburada with Selenium</h1>

> It is a selenium project that gets the first comment from the Hepsiburada website.
<br>

---

## Table of Contents

- [Description](#description)
- [Package](#package)
- [Author](#author)
- [License](#-license)

---

## Description
- Accesses Hepsiburada website via Google Chrome and Firefox browsers.
- Accepts cookies.
- It asks you for input to search.
- Clicks on the 2nd of the listed products.
- Prints the name and price of the product.
- Clicks on comments.
- Saves the first comment to the comment.txt file.
- It saves each step in the log.txt file.

## Package
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
```


## Author

👦🏻 **Yusuf Onaran**

* Github: [@onaranyusuf](https://github.com/onaranyusuf)
* LinkedIn: [@Yusuf Onaran](https://www.linkedin.com/in/yusufonaran/)
* Portfolio: [yusufonaran.me](https://www.yusufonaran.me)

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

This project is under [MIT](https://github.com/onaranyusuf/Hepsiburada-Seleium/blob/main/LICENSE) license.

