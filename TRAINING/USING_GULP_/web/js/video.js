(function(){
 var canvas = document.getElementById('canvas'),
     context = canvas.getContext('2d'),
     video = document.getElementById('video'),
     vendorUrl = window.URL || window.webkitURL;
    navigator.getMedia = navigator.getUserMedia || 
                         navigator.webkitGetUserMedia ||
                         navigator.mozGetUserMedia ||
                         navigator.msGetUserMedia;
    //capture video
    navigator.getMedia({
    	video:true,
    	audio:true
    }, function(stream){

    	video.src =  vendorUrl.createObjectURL(stream);
    	video.play();
    } , function(error){
    	//AN ERROR OCCURED
    	//ERROR CODE
    });
})();


