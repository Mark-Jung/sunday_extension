(function() {
    chrome.browserAction.onClicked.addListener(function (tab) {
        chrome.tabs.create({url: "hi.html"});
        console.log("hallo");
    });
})();
