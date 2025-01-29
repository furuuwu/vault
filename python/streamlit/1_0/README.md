# 1 - Introduction

Goal:

* learning streamlit
* examples from the basics to deployment

Mostly copypasted from

* [docs](https://docs.streamlit.io/)
* [2023 Streamlit for data science, Richards PACKT](https://www.amazon.com/Streamlit-Data-Science-Create-interactive-ebook/dp/B0BTHRBC2W/)

## create a venv, install the dependencies

```none
# requirements.txt

streamlit<2.0.0
matplotlib
```

script that does that for you: `setup_env.sh`

## run the demo

```shell
streamlit hello
```

## run a streamlit program

```shell
streamlit run hello_world.py
```

![a](img/2025-01-28-11-53-59.png)

![a](img/2025-01-28-11-54-48.png)

The users will see the same thing, except for the "Developer options" fields

![a](img/2025-01-28-11-57-34.png)

```shell
streamlit run plot_demo.py
```
