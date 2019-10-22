// export default class Article {
//   ArticleTitle: string;
//   ArticlePath: string;
//   ArticlePid: number;
// }

export default class Article {
	constructor(
		public ArticleTitle: string,
        public ArticleUrl: string,
        public ArticlePath: string,
        public ArticlePid: string,
        public ArticleTime: string,
        public ArticleContent: string
	){}
}