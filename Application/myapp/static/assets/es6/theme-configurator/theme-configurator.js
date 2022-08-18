function colorContrast (hex) {
    if(!hex) {
        return 'dark'
    }
    const threshold = 130;
    const hRed = hexToR(hex);
    const hGreen = hexToG(hex);
    const hBlue = hexToB(hex);
    function hexToR(h) {return parseInt((cutHex(h)).substring(0,2),16)}
    function hexToG(h) {return parseInt((cutHex(h)).substring(2,4),16)}
    function hexToB(h) {return parseInt((cutHex(h)).substring(4,6),16)}
    function cutHex(h) {return (h.charAt(0) === '#') ? h.substring(1,7):h}
    const cBrightness = ((hRed * 299) + (hGreen * 587) + (hBlue * 114)) / 1000;
    if (cBrightness > threshold){
        return 'dark'
    } else { 
        return 'light'
    }	
}

function themeConfigurator() {

    $(document).on('change', 'input[name="header-theme"]', ()=>{
        const context = $('input[name="header-theme"]:checked').val();
        const contrast = colorContrast(context)
        console.log(context, contrast)
        
        $('.header-nav').removeClass (function (index, className) {
            return (className.match (/(^|\s)header-text-\S+/g) || []).join(' ');
        }).addClass( 'header-text-'+ contrast ).css('background-color', context);
    });

    $('#side-nav-theme-toggle').on('change', (e)=> {
        $('.side-nav').toggleClass('nav-menu-dark');
        if(e.target.checked) {
            $('.header-navbar').addClass('nav-menu-dark');
            $('.header-navbar').removeClass('nav-menu-light');
            $('.side-nav .logo img').attr("src", "/assets/images/logo/logo-white.png");
        } else {
            $('.header-navbar').addClass('nav-menu-light');
            $('.header-navbar').removeClass('nav-menu-dark');
            $('.side-nav .logo img').attr("src", "/assets/images/logo/logo.png");
        }
        e.preventDefault();
    });
    
    $('#side-nav-fold-toogle').on('change', (e)=> {
        $('.side-nav').toggleClass('nav-menu-collapse')
        $('.header-nav').toggleClass('is-collapse');
        $('.content').toggleClass('is-collapse')
        if($('.side-nav').hasClass('nav-menu-collapse')) {
            $('.side-nav .logo img').attr('src', `/assets/images/logo/${$('.side-nav').hasClass('nav-menu-dark') ? 'logo-fold-white' : 'logo-fold'}.png`);
        } else {
            $('.side-nav .logo img').attr('src', `/assets/images/logo/${$('.side-nav').hasClass('nav-menu-dark') ? 'logo-white' : 'logo'}.png`);
        }
        e.preventDefault();
    });
}

export default { themeConfigurator }