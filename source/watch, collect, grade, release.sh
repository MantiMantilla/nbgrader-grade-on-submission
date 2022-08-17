#!/bin/bash
inotifywait -m /srv/nbgrader/exchange/HCAD/inbound/ -e create |
    while read dir action file; do
        echo $file
        
        _usr_id=${file%%+*}
        _tmp_dir=${file#*+}
        _tmp_dir=${_tmp_dir%%+*}
	echo "Collecting assignments..."
        nbgrader collect --assignment $_tmp_dir
        
        echo "Grading assignments..."
        nbgrader autograde --assignment $_tmp_dir --student $_usr_id --force
        
        echo "Generating feedback..."
        nbgrader generate_feedback --assignment $_tmp_dir --student $_usr_id  --force
        
        echo "Releasing feedback..."
        nbgrader release_feedback --assignment $_tmp_dir
        
        echo $_tmp_dir
    done
