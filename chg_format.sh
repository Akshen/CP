for i in *.jpeg; do
		sips -s format png $i --out pngs
		done
echo "Operation Over"
