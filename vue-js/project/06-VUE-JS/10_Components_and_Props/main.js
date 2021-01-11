Vue.component("comment",{        //here component name comment
    props: {    // registraion props into component
        comment: { // component properties
            type: Object,
            required: true
        }
    },
    template: `
        <div>
            <div class="card-body">
            <p>{{ comment.username }}</p>
            <p>{{ comment.content }}</p>
        </div>
        <hr>
    `
})

var app = new Vue ({
    el: "#app",
    data: {
        comments : [
            {username: "alice", content: "first comment"},
            {username: "bob", content: "Hello world"},
            {username: "Ironman", content: "new armor coming soon"},
            {username: "superman", content: "kryptonite is bad!"}
        ]
    }
})