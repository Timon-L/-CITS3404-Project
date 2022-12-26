const heightOutput = document.querySelector('#height');
const widthOutput = document.querySelector('#width');
const login = document.getElementById("login");
const sign_up = document.getElementById("sign_up");
const rules = document.getElementById("rules");
const stats = document.getElementById("stats");
const drop_btn = document.getElementById("drop_btn");
const title = document.getElementById("title");
const content = document.getElementById("dropdown_content");
const menu_content = document.getElementsByClassName("menu_content");

let wide_toggle = true;
let menu_toggled = false;

/*  Adjust title position when scaling.
*/
function title_rescale(wide){
    const title_default = {left:"calc(50% - 200px)"};
    const title_scale = {left:"calc(15% - 200px)"};
    if(wide){
        title.style.left = title_default.left;
    }
    else{
        title.style.left = title_scale.left;
    }
}

/*  Hide/display top menu when scaling.
*/
function top_display(wide){
    if(wide){
        login.style.display = "initial";
        sign_up.style.display = "initial";
        rules.style.display = "initial";
        stats.style.display = "initial";
    }
    else{
        login.style.display = "none";
        sign_up.style.display = "none";
        rules.style.display = "none";
        stats.style.display = "none";
    }
}

/*  Hide/display dropdown button when scaling.
*/
function dropdown_display(wide){
    if(wide){
        drop_btn.style.display = "none";
    }
    else{
        drop_btn.style.display = "initial";
    }
}

/*  Re-adjust layout as window width changes.
*/  
function rescale() {
    heightOutput.textContent = window.innerHeight;
    widthOutput.textContent = window.innerWidth;

    if(window.innerWidth < 700 && wide_toggle){
        wide_toggle = false;
        title_rescale(wide_toggle);
        top_display(wide_toggle);
        dropdown_display(wide_toggle);
       
    }
    if(window.innerWidth >= 700 && !wide_toggle){
        wide_toggle = true;
        title_rescale(wide_toggle);
        top_display(wide_toggle);
        dropdown_display(wide_toggle);
    }

}

/*  Hide/display dropdown menu
*   Event: click.
*/
function dropdown_event(){
    drop_btn.addEventListener("click", function(){
        if(!menu_toggled){
            content.style.display = "block";
            menu_toggled = true;
        }
        else{
            content.style.display = "none";
            menu_toggled = false;
        }
    });
    content.addEventListener("mouseleave", function(){
        content.style.display = "none";
        menu_toggled = false;
    })
}

window.onload = function(){
    dropdown_event();
    rescale();
}

window.onresize = rescale;
