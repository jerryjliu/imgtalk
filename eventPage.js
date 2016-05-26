IMAGETALK_ID = "IMAGETALK_ID";

chrome.contextMenus.create({
  "title": "[Imagetalk] Describe Image",
  "contexts": ["image"],
  "id": IMAGETALK_ID,
});

chrome.contextMenus.onClicked.addListener(function(info, tab) {
	if (info.menuItemId == IMAGETALK_ID) {
		// alert(info.srcUrl);
		// var msg = new SpeechSynthesisUtterance('Hello World');
  //   	window.speechSynthesis.speak(msg);
  		alert(info.srcUrl);
  		$.ajax({url:"http://localhost:5000/process?imgurl=" + info.srcUrl,
  			type:"GET", success:function(result){
	  			console.log(result);
	  			alert(result);
	  			var msg = new SpeechSynthesisUtterance(result);
	  			window.speechSynthesis.speak(msg);  			
  		}});
	}
});