class Icon {

    static init() {
        let searchInput = document.querySelector('#search-input');
        searchInput.addEventListener('keyup', search);

        // get all title
        let iconDemo = document.querySelectorAll('.icon-demo-col')
        let searchTerm = '';
        let tit = '';

        function search(e) {
            searchTerm = e.target.value.toLowerCase();

            iconDemo.forEach((title) => {
                tit = title.textContent.toLowerCase();
                console.log(title)
                tit.includes(searchTerm) ? title.style.display = 'block' : title.style.display = 'none';
            });
        }
        
        function copy(value)  {
            const promise = new Promise((resolve) => {
                let copyTextArea = null;
                try {
                    copyTextArea = document.createElement("textarea");
                    copyTextArea.style.height = '0px';
                    copyTextArea.style.opacity = '0';
                    copyTextArea.style.width = '0px';
                    document.body.appendChild(copyTextArea);
                    copyTextArea.value = value;
                    copyTextArea.select();
                    document.execCommand('copy');
                    resolve(value);
                } finally {
                    if (copyTextArea && copyTextArea.parentNode) {
                        copyTextArea.parentNode.removeChild(copyTextArea);
                    }
                }
            });
    
            return (promise);
        }

        function showToast() {
            var toastHTML = `
            <div class="toast align-items-center fade start-50" style="position: fixed; top: 100px; width: 100px" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="d-flex justify-content-center">
                    <div class="toast-body text-center">
                        <i class="icon-check-circle feather text-success"></i>
                        <span>Copied</span>
                    </div>
                </div>
            </div>
            `
        
            $('#notification-toast').append(toastHTML)
            $('#notification-toast .toast').toast('show');
            setTimeout(function(){ 
                $('#notification-toast .toast:first-child').remove();
            }, 1500);
        }

        $('.icon-demo-col').on('click', (e) => {
            const $this = $(e.currentTarget);
            const copiedString = $this.children('.icon-demo').children('.card-body').children('i')[0].className;
            copy(copiedString).then(() => {
                showToast()
            });
        })
    }
    
}

$(() => { Icon.init(); });

