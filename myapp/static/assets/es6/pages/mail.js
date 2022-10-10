class AppMail {

    static init() {

        $('.mail-list-row').on('click', (e) => {
            $('.mail-content').addClass('mobile-show-content')
            $('.mail-list').addClass('mobile-hide-list')
        })

        $('.mail-back').on('click', (e) => {
            $('.mail-content').removeClass('mobile-show-content')
            $('.mail-list').removeClass('mobile-hide-list')
        })

        $('.panel-toggle').on('click', (e) => {
            $('.column-panel').addClass('is-mobile-active')
        })
        $('.panel-toggle-close').on('click', (e) => {
            $('.column-panel').removeClass('is-mobile-active')
        })

        $("#checkAll").on('change',function(){
            $('.mail-list-row input[type="checkbox"]').prop('checked',$(this).is(":checked"));
        }); 

        $('.mail-content-reply').on('click', (e) => {
            $('.mail-reply').removeClass('d-none')
            $('.mail-content-reply').addClass('d-none')
        })

        $('.compose').on('click', (e) => {
            $('.mail-compose').removeClass('d-none')
            $('.mail-content').addClass('d-none')
            $('.mail-list').addClass('d-none')
        })


        new Quill('#mail-reply', {
            theme: 'snow',
            toolbar: [
                ['bold', 'italic', 'underline', 'strike'],        
                ['blockquote', 'code-block'],
                [{ 'header': 1 }, { 'header': 2 }],               
                [{ 'list': 'ordered'}, { 'list': 'bullet' }],
                [{ 'size': ['small', false, 'large', 'huge'] }],  
                [{ 'align': [] }],
                ['link', 'image']                        
            ]
        });

        new Quill('#mail-compose', {
            theme: 'snow',
            toolbar: [
                ['bold', 'italic', 'underline', 'strike'],        
                ['blockquote', 'code-block'],
                [{ 'header': 1 }, { 'header': 2 }],               
                [{ 'list': 'ordered'}, { 'list': 'bullet' }],
                [{ 'size': ['small', false, 'large', 'huge'] }],  
                [{ 'align': [] }],
                ['link', 'image']                        
            ]
        });
    }
}

$(() => { AppMail.init(); });

