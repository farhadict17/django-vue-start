var app = new Vue({
    el: "#app",
    // data: {
    //     // color: "green"
    //     text: '',
    //     checked: true,
    //     city : ''
    // }
    data: {
        comment: null,
        comments: [],
        errors: null
    },
    methods: {
        onsubmit(){
            // let new_comment = this.comment;
            // this.comments.push(new_comment);
            // this.comment = null;
            if(this.comment){
                let new_comment = this.comment;
                this.comments.push(new_comment);
                this.comment = null;
                if (this.errors){
                    this.errors = null;
                }
            }else {
                this.errors = "The comment field can't be empty!"
            }
        }
    }
})