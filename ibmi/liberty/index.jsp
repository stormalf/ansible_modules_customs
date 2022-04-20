<!DOCTYPE html>
<html lang="en">
  <head>
    <title>JSP Test</title>
    <%! String title = "Hello World"; %>
  </head>
  <body>
    <h2><%= title %></h2>
    <p>
      If you see this, the example war-file was correctly deployed! Congrats!
    </p>
    <p><%= new java.util.Date() %></p>
    <div id="conrgrats"></div>
  </body>
</html>
