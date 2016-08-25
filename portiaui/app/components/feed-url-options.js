import Ember from 'ember';
const { computed } = Ember;

export default Ember.Component.extend({
    isEditing: computed('startUrl.url', function() {
        return this.get('startUrl.url') === '';
    })
});
