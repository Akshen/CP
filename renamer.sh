count=0 
for i in *.png; do
		mv "$i" "normal_img${count}.png";
		let count++;
done
echo "Operation Complete..."
