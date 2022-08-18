const sideNav = '.side-nav'
const navMenuCollapse = 'nav-menu-collapse'
const navMenuQuickExpand = 'nav-menu-quick-expand'

export default class Core {

    constructor() {
		this.sideNav();
		this.pfScrollBar();
		this.tooltipInit();
		this.popOverInit();
		this.toastInit();
		this.headerNav();
	}

	setLogo() {
		if($(sideNav).hasClass(navMenuCollapse) && !$(sideNav).hasClass(navMenuQuickExpand)) {
			$(`${sideNav} .logo img`).attr('src', `/assets/images/logo/${$(sideNav).hasClass('nav-menu-dark') ? 'logo-fold-white' : 'logo-fold'}.png`);
		} else {
			$(`${sideNav} .logo img`).attr('src', `/assets/images/logo/${$(sideNav).hasClass('nav-menu-dark') ? 'logo-white' : 'logo'}.png`);
		}
	}

	toggleNavMenuQuickExpand(action, e) {
		const $this = $(e.currentTarget);
		if($this.hasClass(navMenuCollapse)) {
			$(sideNav)[action]('nav-menu-quick-expand')
			this.setLogo()
		}
	}

	headerNav() {
		$('.header-nav .desktop-toggle').on('click', () => {
			$(sideNav).toggleClass(navMenuCollapse)
			$('.header-nav').toggleClass('is-collapse')
			$('.content').toggleClass('is-collapse')
			$('.desktop-toggle .nav-icon').toggleClass('icon-menu')
			this.setLogo()
		});

		$('.header-nav .mobile-toggle').on('click', () => {
			$(sideNav).addClass('is-opened')
		})
	}
	
    sideNav() {
		const active = 'active';
		const drodpDownItem = '.vertical-menu .nav-menu .nav-submenu .nav-menu .nav-menu-item';	

		if ($(drodpDownItem).hasClass(active)) {
			$( drodpDownItem + '.' + active).parent().parent().addClass('open') 
		}

        $('.vertical-menu .nav-menu li a').on('click', (e) => {
			const $this = $(e.currentTarget);

			if ($this.parent().hasClass("open")) {

				$this.parent().children('.nav-menu').slideUp(200, ()=> {
					$this.parent().removeClass("open");
				});

			} else {
				$this.parent().parent().children('li.open').children('.nav-menu').slideUp(200);
				$this.parent().parent().children('li.open').children('a').removeClass('open');
				$this.parent().parent().children('li.open').removeClass("open");
				$this.parent().children('.nav-menu').slideDown(200, ()=> {
					$this.parent().addClass("open");
				});
			}
		});

		$(`${sideNav} .nav-logo .mobile-close`).on('click', () => {
			$(sideNav).removeClass('is-opened')
		})

		$(`${sideNav}`).on('mouseenter', e => {
			this.toggleNavMenuQuickExpand('addClass', e)
		}).on('mouseleave', e => {
			this.toggleNavMenuQuickExpand('removeClass', e)
		});

	} 

	pfScrollBar() {
		$('.scrollable').perfectScrollbar();
	}
	
	tooltipInit() {
		$('[data-toggle="tooltip"]').tooltip()
	}

	popOverInit() {
		const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
		popoverTriggerList.map(function (popoverTriggerEl) {
			return new bootstrap.Popover(popoverTriggerEl)
		})

	}

	toastInit() {
		$('.toast').toast();
	}
}    