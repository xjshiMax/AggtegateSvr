#! /bin/bash
codePATH=../PythonHelpServer.py
while :
do
case "$(pgrep -f "python $codePATH" | wc -w)" in 
0)  echo "Starting program:     $(date)" >> /mnt/code/shdir/log
    python $codePATH &    
    ;;
*)  echo "running    $(pgrep -f "python $codePATH" | wc -w)           $(date)" >> ../pyserverlog/log  
    ;;
  
esac
sleep 10
done
