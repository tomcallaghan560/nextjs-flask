cd server

python -m venv venv activated below

![1748859262897](image/README/1748859262897.png)


activate env [name_of_env]\Scripts\activate.bat

need server.py to write all of flask code in

pip install flask

cd ../client

npx create-next-app . // . to make create in this directory

made server.py code to send message to frontend

python server.py

ctrl c to quit server

cls to clean terminal

https://localhost:3000

get rid of nextjs boilerplate code

want to set up page to display our message Hello World

remove all code in index.tsx

remove all code in globals.css keep 

@tailwind base;

@tailwind components;

@tailwind utilities;

Need cores to make request from nextjs server to python server o.w. get cross origin issue

cd server
