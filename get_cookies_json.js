function cookiesToJSON() {
    let cookies = document.cookie.split('; ');
    let cookieObj = {};

    cookies.forEach(cookie => {
        let [name, value] = cookie.split('=');
        cookieObj[name] = decodeURIComponent(value);
    });

    return JSON.stringify(cookieObj, null, 2);
}

let jsonText = cookiesToJSON();
console.log(jsonText);