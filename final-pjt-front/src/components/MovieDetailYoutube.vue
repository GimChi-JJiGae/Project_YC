<template>
    
  <div>
    <div v-show="false">
        {{movieYoutubeUrl}}
    </div>
    <iframe width="560" height="315" :src="this.youtubeLink" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div>
</template>

<script>


export default {
    name : "MovieDetailYoutube",
    data : function() {
        return {
            movieUrl : this.movieYoutubeUrl,
            youtubeLink : ''
        }
    },
    props : {
        movieYoutubeUrl : String
    },
    methods: {
     getYoutube : function() {
        
        
        
        fetch(this.movieYoutubeUrl)
            .then(res => res.json())
            .then((res) =>{
                
                if(res.results.length > 0){
                        const youtubeId = res.results[0].key//첫번재 영상만 사용하기 하자. 값이 없을 경우도 있음.
                       
                        //this.youtubeLink = `<iframe width="100%" height="100%" src="https://www.youtube.com/embed/${youtubeId}?autoplay=1"></iframe>`;
                        this.youtubeLink = `https://www.youtube.com/embed/${youtubeId}?autoplay=1`  
                        
                    } else {
                        //output = `<h3 class="noVideo">재생할 예고편이 없습니다.</h3>`;
                        //console.log(output);
                    }
            })
        
     }
    },
    updated : function() {
        this.getYoutube()
       
    }

}
</script>

<style>

</style>