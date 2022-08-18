class UserList {

    static init() {
        $('.user-list-table').DataTable({
            'columnDefs': [
                { 'orderable': false, 'targets': 0 }
            ]
        });
    }
}

$(() => { UserList.init(); });

