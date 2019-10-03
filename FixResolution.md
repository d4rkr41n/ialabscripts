## Use this to get the 1920x1080 res as an option if it isn't    
### Snag modeline    
` gtf 1920 1080 60 `

### Tell the system about your new mode    
` xrandr --newmode <result from above be careful> `    
*__//eg.__ "1920x1080_60.00"  172.80  1920 2040 2248 2576  1080 1081 1084 1118  -HSync +Vsync*    

### Add the mode to the display (Probably Virtual1, you can check with ` xranr --query `)    
` xrandr --addmode Virtual1 "<first part from your newmode>" `    
*__//eg.__ ` xrandr --addmode Virtual1 "1920x1080_60.00" `*    
