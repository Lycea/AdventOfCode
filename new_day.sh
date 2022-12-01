

echo "Creating new folder" 

y=$(date +"%Y") 
echo "   Using year $y"
echo "   Using day $1"

cp -r template $y/$1
exit

arg_1_length=$( expr length $1 )
arg_2_length=$( expr length $2 )

if [  #$1 -eq 4 ] 
then
  y=$1
else
  y=$(date +"%Y") 
fi





