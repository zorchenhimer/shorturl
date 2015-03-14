runesenabled = false;

function enable_runes() {
    music_tags = document.getElementsByTagName('h1');
    runetags = document.getElementsByClassName('text');
    for(var i = 0; i < music_tags.length; i++) {
        music_tags[i].className = 'musicrunes';
    }
    for(var i = 0; i < runetags.length; i++) {
        runetags[i].className = 'runes';
    }
}

function disable_runes() {
    music_tags = document.getElementsByTagName('h1');
    runetags = document.getElementsByClassName('runes');
    for(var i = 0; i < music_tags.length; i++) {
        music_tags[i].className = '';
    }
    for(var i = 0; i < runetags.length; i++) {
        runetags[i].className = 'text';
    }
}

function toggle_runes() {
    /* i hate javascript. */
    if(runesenabled == false) {
        enable_runes();
        enable_runes();
        enable_runes();
        runesenabled = true;
    } else {
        disable_runes();
        disable_runes();
        disable_runes();
        runesenabled = false;
    }
}


