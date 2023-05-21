$(function () {
  var mainpc01 = $("#slidertype1");
  var mainpc02 = $("#slidertype2");
  var mainpc03 = $("#slidertype3");
  var mainpc04 = $("#slidertype4");
  var mainpc05 = $("#slidertype5");

  var slide_num = 3; //Number of pictures
  var fadeSpeed = 1500; //Speed of fade
  var countspeed = 2700; //Picture stopping time
  var countspeed2 = fadeSpeed - 100; //Time delay between the two pictures

    var count = 1;
    var pic_num = 1;
    var stop_count = 1;

    function loop() {
      if (count == 1) {
        //photo on
        $("#slidertype" + pic_num)
        .css({ display: "block", opacity: "0" })
		.animate({ opacity: "1" }, fadeSpeed);
      } else if (count == 2) {
        //photo off
        $("#slidertype" + pic_num)
		.css({ display: "block", opacity: "1" })
		.animate({ opacity: "0" }, fadeSpeed);
      } else if (count == 3) {
        //hide the photo
        $("#slidertype" + pic_num).hide();

        //Next photo
        pic_num = pic_num + 1;
        stop_count = stop_count + 1;
        $("#slidertype" + pic_num)
		.css({ display: "block", opacity: "0" })
		.animate({ opacity: "1" }, fadeSpeed);
      }

      count = count + 1;

	if (stop_count != slide_num) {
		if (count == 4) { count = 2;}
		if (count == 2) { setTimeout(loop, countspeed); } 
		else if (count == 3) { setTimeout(loop, countspeed2); }
	}
    };
});
