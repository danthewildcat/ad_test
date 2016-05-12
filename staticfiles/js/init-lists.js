var ListItem = Backbone.Model.extend({

});

var ItemCollection = Backbone.Collection.extend({
    model: ListItem,
    
    initialize: function(opts){
    },
    
    url: '/api/v1/item'
});

var ShoppingList = Backbone.Model.extend({
    defaults: {
        items: new ItemCollection()
    }
});

var ShoppingListView = Backbone.View.extend({
    template: _.template('<a href="#!" class="collection-item"><%= label %></a>'),
    
    initialize: function(){
        
    },
    
    render: function(){
        
    }
});

var ListCollection = Backbone.Collection.extend({
    model: ShoppingList,
    
    initialize: function(models, opts){
        this.fetch();  
    },
    
    url: '/api/v1/shopping'
});

$(document).ready(function(){
    var $lists = $( '#shopping_lists.collection', this);
    var list = new ListCollection({ el: $lists[0] });
    
    var $new_list = $('#new_list.btn', this);
    $new_list.click(function(e){
    });
});
