#!/usr/bin/python3

print("Content-type:text/html\n\n")

body = """
<!DOCTYPE html>
<html>
<head>
<title>
    Title
</title>
  <link rel="stylesheet" type="text/css" href="https://webapp.mel.setec.com.au/static/ate/css/table_lot.css"/>
  <link rel="stylesheet" type="text/css" href="https://webapp.mel.setec.com.au/static/admin/css/base.css"/>
  <link rel="stylesheet" type="text/css" href="https://webapp.mel.setec.com.au/static/admin/css/changelists.css"/>
  <link rel="stylesheet" type="text/css" href="https://webapp.mel.setec.com.au/static/admin/css/forms.css"/>

<script type="text/javascript">
function hide_show_table(col_name)

// Add functionality to specify multiple column names when hiding

{{
 //var obj = {{}};
 //for(var i=0, l = col_names.length; i < l; i++){{
 //col_name = obj[col_names[i]]

 var checkbox_val=document.getElementById(col_name).value;
 if(checkbox_val=="hide")
   {{
     var all_col=document.getElementsByClassName(col_name);
     for(var i=0;i<all_col.length;i++)
     {{
       all_col[i].style.display="none";
     }}
   document.getElementById(col_name+"_head").style.display="none";
   document.getElementById(col_name).value="show";
   }}
else
  {{
    var all_col=document.getElementsByClassName(col_name);
    for(var i=0;i<all_col.length;i++)
  {{
    all_col[i].style.display="table-cell";
  }}
    document.getElementById(col_name+"_head").style.display="table-cell";
    document.getElementById(col_name).value="hide";
  }}
}}

</script>

</head>
<body>
<div id="container"><div id="body">
<div id="content" class="flex">
    <h1>A Title : {}</h1>
<div class="results">
""".format('a_placeholder')  #lot_placeholder is replaced once we know the lot.


chechbox_html = """
<div id="checkbox_div">
 <input type="checkbox" value="hide" id="hide_me" onchange="hide_show_table(this.id);"> Hide Columns 1 and 5
</div>
"""
body += chechbox_html


html_table = """
<table>
<tr><th id="hide_me_head">col1</th><th>col2</th><th>col3</th><th>col4</th><th>col5</th></tr>
<tr><td class="hide_me">a</td><td>a1</td><td>c</td><td>e</td><td>g</td></tr>
<tr><td class="hide_me">b</td><td>b1</td><td>d</td><td>f</td><td>h</td></tr>

</table>
"""
body += html_table

print(body)
