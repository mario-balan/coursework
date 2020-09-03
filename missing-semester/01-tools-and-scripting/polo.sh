#!/bin/bash

echo 'Polo!'
marco=$(find ../../../ -name 'find_me_here')
cd $(dirname "$marco")
rm 'find_me_here'
