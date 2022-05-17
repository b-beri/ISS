texts = ["B.B.", "Bhav", "Beri", "Student", "Coder"];

index = 0;
charIndex = 0;
front_back = 0;
speed = parseInt(prompt("Characters Speed", "300"));


function typing() {
    if (charIndex < texts[index].length && !front_back) {
        document.getElementById("typingFrame").innerText += texts[index][charIndex];
        charIndex++;
        // setTimeout(typing, speed);
    }
    else if (charIndex == texts[index].length && !front_back) {
        front_back = 1;
        document.getElementById("typingFrame").innerText = texts[index].substring(0, charIndex - 1);
        charIndex--;
        //  setTimeout(typing, speed);
    }
    else if (charIndex <= 0 && front_back) {
        index = (index + 1) % (texts.length);
        front_back = 0;
        document.getElementById("typingFrame").innerText += texts[index][charIndex];
        charIndex++;
        // setTimeout(typing, speed);
    }
    else if (charIndex < texts[index].length && front_back) {
        document.getElementById("typingFrame").innerText = texts[index].substring(0, charIndex - 1);
        charIndex--;
        // setTimeout(typing, speed);
    }

}
setInterval(typing, speed)

typing();