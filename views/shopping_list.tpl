<html>
<body>
<table>
% for item in shopping_list:
  <tr>
    <td>{{str(item['id'])}}</td>
    <td>{{str(item['description'])}}</td>
  </tr>
% end
</table>
</body>
</html>
