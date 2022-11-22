<template>
  <div>
    <div class="row">
      <div class="col-12 col-lg-6">
        <a :href="`https://www.themoviedb.org/movie/${movie.id}`">
          <img
            :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
            width="400"
            height="600"
            alt=""
          />
        </a>
      </div>

      <div class="col-12 col-lg-6">
        <h1>{{ this.movie.title }}</h1>

        <div>
          <StarRating
            :rating="parseFloat(movie.vote_average) / 2"
            :read-only="true"
            :increment="0.01"
          />
        </div>
        {{ this.movie.overview }}
        <h1>감독</h1>
        <div v-if="called">
          <a :href="`https://www.themoviedb.org/person/${directorId}`">
            <img
              :src="`https://image.tmdb.org/t/p/original/${directorProfile}`"
              width="100"
              height="150"
              alt=""
            />
          </a>
        </div>
        <h1>배우</h1>
        <div v-if="called">
            
                <span v-for="i in list" :key="i">
                <a :href="`https://www.themoviedb.org/person/${actorsId[i]}`">
                    <img
                    :src="`https://image.tmdb.org/t/p/original/${actorsProfile[i]}`"
                    width="100"
                    height="150"
                    alt=""
                    />
                </a>
            </span>
           
        </div>
        <!--<MovieDetailTopCredit v-if="directorId" directorId :directorProfile="directorProfile"/>-->

        <span></span>
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from "vue-star-rating";
import axios from "axios";
//import MovieDetailTopCredit from './MovieDetailTopCredit.vue';

export default {
  name: "MovieDetailTop",
  components: {
    StarRating,
    //MovieDetailTopCredit,
  },
  props: {
    movie: Object,
  },
  data: function () {
    return {
      list: [0, 1, 2, 3, 4],
      called: false,
      movie_overview: "",
      rating: Number(this.movie.vote_average) / 2,
      //creditUrl : `https://api.themoviedb.org/3/movie/${this.movie.id}/credits?api_key=5d2592924ae354925561438e12ee8888&language=en-US`
      actorsId: [],
      actorsProfile: [],
      directorId: "",
      directorProfile: "",
    };
  },
  methods: {
    getCredit: function () {
      const movie_data = JSON.parse(localStorage.getItem('movie_list'))[this.$route.params.movie_pk - 1]
      const movie_original_id = movie_data.original_id
      axios
        .get(
          'https://api.themoviedb.org/3/movie/'+ movie_original_id +'/credits?api_key=5d2592924ae354925561438e12ee8888&language=en-US'
        )
        // .then((res) => {
        //   res.json();
        // })
        .then((res) => {
          console.log(res);
          for (let i = 0; i < 5; i++) {
            this.actorsId.push(res.data.cast[i].id);
            this.actorsProfile.push(res.data.cast[i].profile_path);
          }
          const director = res.data.crew.filter(({ job }) => job === "Director");
          this.directorProfile = director[0].profile_path
          this.directorId = director[0].id
          this.called = true;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    console.log("hi");
    this.getCredit();
  },
};
</script>

<style>
</style>