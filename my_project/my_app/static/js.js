function changeImage(e) {
    img_elem = document.getElementById("img_id")
    cur_img = img_elem.src
    image_num = cur_img.split("/")[4].split(".")[0]       
    new_image = (Number(image_num) + 1) % 5 + 1
    new_image = `http://127.0.0.1:8000/static/${new_image}.jpg`    
    img_elem.src = new_image
}