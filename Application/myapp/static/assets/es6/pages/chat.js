class Chat {

    static init() {
        $('.conversation .panel-toggle').on('click', () => {
            $('.column-panel').addClass('is-mobile-active')
        })

        $('.chat-panel .chat-list-row').on('click', () => {
            $('.column-panel').removeClass('is-mobile-active')
        })
    }
}

$(() => { Chat.init(); });

