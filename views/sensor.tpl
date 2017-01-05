from bottle import template
<html>
<head>
</head>
<body>
  <form name="edit" method="POST" action="">
    <table>
      <tr><th>名称</th><th>値</th></tr>
      <tr><td>ID</td><td><textarea name="id" value="{{id}}"/></td></tr>
      <tr><td>名称</td><td><textarea name="name" value="{{name}}"/></td></tr>
      <tr><td>ピン番号</td><td><textarea name="pinNo" value="{{pinNo}}"/></td></tr>
      <tr><td>有効</td><td><textarea name="available" value="{{available}}"/></td></tr>
      <tr><td>入出力</td><td><textarea name="direction" value="{{direction}}"/></td></tr>
      <tr><td>ピン指定方式</td><td><textarea name="mode" value="{{mode}}"/></td></tr>
    </table>
  </form>
</body>
</html>
