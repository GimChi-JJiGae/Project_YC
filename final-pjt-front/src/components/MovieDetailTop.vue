<template>
  <div>
    <div class="row align-items-center justify-content-center">
      <div class="col-12 col-lg-6 p-3" style="height:100%">
        <a :href="`https://www.themoviedb.org/movie/${movie.id}`">
          <img
            :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
            alt=""
            style="width:100%; max-width: 500px; object-fit: cover;"
            class="rounded-3"

          />
        </a>
      </div>

      <div class="col-12 col-lg-6 row justify-content-center" style="height:100%">
        <div class="row align-items-center mb-2">
          <div class="col">
            <h1 class="m-0">{{ this.movie.title }}</h1>
          </div>
        </div>
        <div class="row align-items-center mb-3">
          <div class="col">
            <StarRating
            active-color="#FF8C0A"
            :rating="parseFloat(movie.vote_average) / 2"
            :read-only="true"
            :increment="0.01"
            :star-size="40"
            />
          </div>
          <div class="col">
            <button class="btn content-font border btn-sm" style="height:36px; min-width: 56px;" @click="open">
              <span style="font-size: 15px;">예고편</span>
            </button>
          </div>
          <div class="col-2" @click="likeMovie">
            <font-awesome-icon icon="fa-regular fa-heart" /> {{ this.like_numbers }}
          </div>
        </div>
        <div class="row">
          {{ this.movie.overview }}
        </div>
        <div class="row text-start mb-3">
          <div >
            <h3>감독</h3>
          </div>
          <div v-if="called">
            <a :href="`https://www.themoviedb.org/person/${directorId}`">
              <img
              :src="`https://image.tmdb.org/t/p/original/${directorProfile}`"
              width="100"
              height="150"
              alt=""
              onerror="this.src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAAIVBMVEXY2Njz8/Pq6urv7+/h4eHb29vo6Oje3t7j4+Pt7e3p6ekmc3lwAAADMElEQVR4nO2bC3KDMAxEMeab+x+4JZQBEkhBlq2NZt8JvGOtPkZUFSGEEEIIIYQQQgghhBBCCCEEnXbo6hjDLzHW3dBan0dEO9ThjfrrxDQHKv60NNZnu0ETz2Q8w+xbpPQfZTyl9NZnvEB7GlS7AIP3SnNFxgR4fHVXdYTQWZ/1A+14XUcII2x4tf+6fE8EVXJXB6qS+zpAldzyx8Jofep3buSrLXC563L9eAWsnrRSHSFg2eRSX3JMbX32Lb1cRwhIHaQg865E69OviJ0+g+P3pAsBupLEC8G5koSUNQOSuBJqyAJGLRnShQzWGp4kRxZKbKXrCMFaw4SCRTBMomARDJMIB5E9CGOJgtcx3J7Yn8wgdCluhGjogMi/FEIhmXBjdjdC3BRENy2Km6bRTRvvZrDyM+q6eXxw8xzk5oHOz5Opm0dsP58V3Hzo8fPpzc3HUD+fp90sDPhZ4fCzVONnzcnN4pmfVUA/y5mVm3XZys8Cs5+V8srNkv+Ek98uJpz8CDPh5NekGRc/ixFCCCHky2mb4TGO8cLkHuM4PoYGsGfph1r0Ih/rAWc2Oexz74DRE59PHre0GE8pvcoiykxnF2O96Ln3nNFGSqMs4ymlfIT9/1Qio/ADS6vojVe6gilMZUXrnFKbKfeeqiWUed5OXti4QgHTZ3THltxv9fnDaiFveOVKukfkTMRJmxr3yaakiM23ZLJ8cR2ZlBjoyKKksD8W1H1ipENdiWQ/QwflrYJidfAd1b2bQn3JMYrdiknCWlFLXSo/VqSgZRNDg8wo2STzPHgFlZnRPLAmNILLNGMtKGQus5K+J73Am5X0PckL9MYlZCW1mJin3oXEFAzikIk0l8BcSOKVAF1I2pVA1JCFlFpiffY9ch0wuXdGnoFVvnPqIf6JCaJd3CJtHQH69z3Sbh4ssuSxZX3ud2Q6oKrhjKwmwllEahI4i0hNAjJSbZGNV9anPkKiA64cTkhKIlijNSNptwCTlixtPawPfcRDIARoyl2RzLtuhACWEVkhcSPE+szHUAgaFIIGhaBBIWhQCBoUggaFoEEhaFAIGhSCBoWgQSFoUAgap8f9Ac1KQOtCVp1TAAAAAElFTkSuQmCC'"
              />
              
            </a>
            <p>{{directorName}}</p>
          </div>
        </div>
        <div class="row text-start mb-3" >
          <div>
            <h3>배우</h3>
          </div>
          <div v-if="called" >
            <div class="row flex-nowrap" id="scollbar" style="height:100%">
              <span v-for="i in list" :key="i" style="width:110px;">
                <a :href="`https://www.themoviedb.org/person/${actorsId[i]}`">
                  <img
                  :src="`https://image.tmdb.org/t/p/original/${actorsProfile[i]}`"
                  style="width:100px; height: 150px;"
                  class="rounded-2"
                  onerror="this.src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAAIVBMVEXY2Njz8/Pq6urv7+/h4eHb29vo6Oje3t7j4+Pt7e3p6ekmc3lwAAADMElEQVR4nO2bC3KDMAxEMeab+x+4JZQBEkhBlq2NZt8JvGOtPkZUFSGEEEIIIYQQQgghhBBCCCEEnXbo6hjDLzHW3dBan0dEO9ThjfrrxDQHKv60NNZnu0ETz2Q8w+xbpPQfZTyl9NZnvEB7GlS7AIP3SnNFxgR4fHVXdYTQWZ/1A+14XUcII2x4tf+6fE8EVXJXB6qS+zpAldzyx8Jofep3buSrLXC563L9eAWsnrRSHSFg2eRSX3JMbX32Lb1cRwhIHaQg865E69OviJ0+g+P3pAsBupLEC8G5koSUNQOSuBJqyAJGLRnShQzWGp4kRxZKbKXrCMFaw4SCRTBMomARDJMIB5E9CGOJgtcx3J7Yn8wgdCluhGjogMi/FEIhmXBjdjdC3BRENy2Km6bRTRvvZrDyM+q6eXxw8xzk5oHOz5Opm0dsP58V3Hzo8fPpzc3HUD+fp90sDPhZ4fCzVONnzcnN4pmfVUA/y5mVm3XZys8Cs5+V8srNkv+Ek98uJpz8CDPh5NekGRc/ixFCCCHky2mb4TGO8cLkHuM4PoYGsGfph1r0Ih/rAWc2Oexz74DRE59PHre0GE8pvcoiykxnF2O96Ln3nNFGSqMs4ymlfIT9/1Qio/ADS6vojVe6gilMZUXrnFKbKfeeqiWUed5OXti4QgHTZ3THltxv9fnDaiFveOVKukfkTMRJmxr3yaakiM23ZLJ8cR2ZlBjoyKKksD8W1H1ipENdiWQ/QwflrYJidfAd1b2bQn3JMYrdiknCWlFLXSo/VqSgZRNDg8wo2STzPHgFlZnRPLAmNILLNGMtKGQus5K+J73Am5X0PckL9MYlZCW1mJin3oXEFAzikIk0l8BcSOKVAF1I2pVA1JCFlFpiffY9ch0wuXdGnoFVvnPqIf6JCaJd3CJtHQH69z3Sbh4ssuSxZX3ud2Q6oKrhjKwmwllEahI4i0hNAjJSbZGNV9anPkKiA64cTkhKIlijNSNptwCTlixtPawPfcRDIARoyl2RzLtuhACWEVkhcSPE+szHUAgaFIIGhaBBIWhQCBoUggaFoEEhaFAIGhSCBoWgQSFoUAgap8f9Ac1KQOtCVp1TAAAAAElFTkSuQmCC'"
                  alt=""
                  />
                </a>
                <p>{{ actorsName[i]}}</p>
              </span>
            </div>
          </div>
        </div>
      </div>
        <!--<MovieDetailTopCredit v-if="directorId" directorId :directorProfile="directorProfile"/>-->
    </div>
    <b-modal
          hide-footer
          v-model="show"
          v-if="show"
          id="youtube-modal"
          size="xl"
          title="Youtube Trailer"
          hide-header-close
        >
          <section class="page-section" id="contact">
            <div>
              <iframe width="100%" height="600px" :src="this.youtubeLink" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            <div>
              <button @click="close" class="m-1 btn content-font border btn-sm" type="submit">닫기</button>
            </div>
          </section>
        </b-modal>
  </div>
</template>

<script>
const SERVER_URL = 'http://127.0.0.1:8000'
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
      // movieYoutubeUrl : `https://api.themoviedb.org/3/movie/${this.movie.id}/videos?api_key=5d2592924ae354925561438e12ee8888`,
      list: [0, 1, 2, 3, 4],
      called: false,
      movie_overview: "",
      rating: Number(this.movie.vote_average) / 2,
      //creditUrl : `https://api.themoviedb.org/3/movie/${this.movie.id}/credits?api_key=5d2592924ae354925561438e12ee8888&language=en-US`
      actorsId: [],
      actorsProfile: [],
      actorsName: [],
      directorId: "",
      directorProfile: "",
      directorName: "",
      like_numbers: null,
      show: false,
      youtubeLink: null,
    };
  },
  computed: {
    movieYoutubeUrl() {
      return `https://api.themoviedb.org/3/movie/${this.movie.id}/videos?api_key=5d2592924ae354925561438e12ee8888`
    },
    isLogin() {
      const checkToken = localStorage.getItem('access_token')
      if(checkToken === null){
        return false
      }
      else {
        return true
      }
    }
  },
  methods: {
    getCredit: function () {
      const movie_data = JSON.parse(localStorage.getItem('movie_list'))[this.$route.params.movie_pk - 1]
      const movie_original_id = movie_data.original_id
      console.log('1')
      axios
      .get(
        'https://api.themoviedb.org/3/movie/'+ movie_original_id +'/credits?api_key=5d2592924ae354925561438e12ee8888&language=en-US'
        )
        // .then((res) => {
          //   res.json();
          // })
        .then((res) => {
          for (let i = 0; i < 5; i++) {
            this.actorsId.push(res.data.cast[i].id)
            this.actorsProfile.push(res.data.cast[i].profile_path)
            this.actorsName.push(res.data.cast[i].name)
          }
          console.log(this.actorsName)
          const director = res.data.crew.filter(({ job }) => job === "Director");
          this.directorProfile = director[0].profile_path
          this.directorId = director[0].id
          this.directorName = director[0].name
          this.called = true;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getToken() {
      const token = localStorage.getItem('access_token')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    likeMovie: function () {
      if (!this.isLogin){
        alert("좋아요 기능을 사용하시려면 로그인을 해주세요")
        this.$router.push({ name: 'LogInView' })
        return
      }
      
      const config = this.getToken()
      axios.post(`${SERVER_URL}/movies/${this.$route.params.movie_pk}/likes/`, this.is_Like, config)
        .then(res => {
          this.is_liked = res.data.is_liked
          this.like_numbers = res.data.likes_count
          // this.getArticleDetail()
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateInfo(){
      axios.get(`${SERVER_URL}/movies/${this.$route.params.movie_pk}/get_likes/`)
        .then(res => {
          this.like_numbers = res.data.likes_count
          // this.getArticleDetail()
        })
        .catch(err => {
          console.log(err)
        })
    },
    open() {
      this.show = true
      this.getYoutube()
    },
    close() {
      this.show = false
    },
    getYoutube() {
      fetch(this.movieYoutubeUrl)
        .then(res => res.json())
        .then((res) =>{
          if(res.results.length > 0){
            const youtubeId = res.results[0].key//첫번재 영상만 사용하기 하자. 값이 없을 경우도 있음.
            //this.youtubeLink = `<iframe width="100%" height="100%" src="https://www.youtube.com/embed/${youtubeId}?autoplay=1"></iframe>`;
            this.youtubeLink = `https://www.youtube.com/embed/${youtubeId}?autoplay=1`    
          }
      })
    },
  },
  created() {
    this.getCredit();
    this.updateInfo();
    
  },
};
</script>

<style>
.modal-dialog.modal-80size {
  width: 80%;
  height: 80%;
  margin: 0;
  padding: 0;
}

.modal-content.modal-80size {
  height: auto;
  min-height: 80%;
}

#scollbar {
  overflow: auto;
  width: 100%;
}
#scollbar::-webkit-scrollbar {
  width: 5px;
  height: 10px;
  /* display: none; */
}
#scollbar::-webkit-scrollbar-thumb {
  background-color: #2f3542;
  border-radius: 10px;
  background-clip: padding-box;
  border: 1px solid transparent;
}
#scollbar::-webkit-scrollbar-track {
  background-color: grey;
  border-radius: 10px;
  box-shadow: inset 0px 0px 5px white;
}
</style>