var app = new Vue ({
    el: "#app",
    data: {
        first_name: "John",
        last_name : "Doe"
    },
    // computed properties use same value from cache until change the value this is the diff with method
    computed: {
        getRandomComputed(){
            return Math.random();
        },
        fullName(){
            //return `${ this.first_name } ${this.last_name}`;
            first = this.first_name;
            last = this.last_name
            return `${first} ${last}`
        },
        reversedFullName(){
            first = this.first_name.split("").reverse().join("")
            last = this.last_name.split("").reverse().join("")
            return `${first} ${last}`
        }
    },
    methods: {
        getRandomNumber(){
            return Math.random();
        }
    }
})