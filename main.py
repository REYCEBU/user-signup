from flask import Flask, request, redirect, render template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = ""

<!DOCTYPE html>
<html>
  <head>
    <title>Please Sign Up</title>
    <style>
      div {
          margin-bottom: 5px;
      }
      label {
          display: block;
          float: left;
          width: 150px;
          text-align: right;
          font-weight: bold;
          margin-right: 10px;
      }
      input.submit {
          margin-left: 160px;
      }
    </style>
</head>
<body>
  <h1> Please Sign Up</h1>
  <form action="/form-processing-script" method="post">
    <div>
      <label for="username">Username</label> <input type="text" name="username">
    </div>
    <div>
      <label for="password">Password</label> <input type="password" name="password">
    </div>
    <div>
      <input type="submit" class="submit" value="Submit">
    </div>
  </form>
</body>
</html>


