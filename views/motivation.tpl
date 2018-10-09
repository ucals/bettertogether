% include('header.tpl')
<div class="container">
    <div class="row">
        <div class="col-md-8 offset-md-2 col-xs-12 col-sm-10 offset-sm-1">
            <h1 class="text-center">#bettertogether</h1>
            <br/>
            <h4>Motivation</h4>
            <p>My first motivation to start this work came from my personal struggle to form a team, to work in OMSCS EdTech final project. In spite of deeply believing that we perform much better when working in teams, I could not successfully do it.<p>
            <p>After the first assignments, I was approached by few students who read some of my essays, and decided to choose among them after reading their work. This would take some time, but I believed it would be worth. However, as the days passed, I continued to be approached, and the list of work to read from potential prospects grew larger: new potential prospects' work, and more work from old potential prospects.<p>
            <p>On top of being approached, by providing feedback to other students, I became very curious about some of them. "I'd love to have time to read their work as well and maybe invite them to work together", I thought. But by then, the list of work to read, to select potential prospects and form a team, was already over 100 documents. How would I find time to read them all? Isn't there a better way?<p>
            <p>Then, I started to research Natural Language Processing tools. I'm very interested in Artificial Intelligence, especially NLP: today, AI is solving challenges in several areas that would have been impossible few years ago. To my surprise, I found a lot of great libraries, well written papers and tutorials, and easy-to-use tools (if you are willing to read their documentation, and try/experiment a lot). <p>
            <p>Instead of reading close to 1,000 essays from fellow students (~200 students in class x 5 essays/student), I decided to read few tutorials, papers and documentation to build a tool to do it for me! Basically, this problem could be solved by calculating similarity score (distance) between pairs of documents. My second motivation was this: learning new NLP techniques, to improve my AI/Machine Learning skills.<p>
            <p>Thanks to <a href="https://cs.stanford.edu/~quocle/paragraph_vector.pdf" target="_blank" rel="noopener noreferrer">Doc2Vec from Stanford</a>, <a href="https://radimrehurek.com/gensim/" target="_blank" rel="noopener noreferrer">Gensim Python library</a>, <a href="https://www.textrazor.com/" target="_blank" rel="noopener noreferrer">TextRazor API</a> and several heroes who take the time to help others by publishing their work online for free, 21 hours after the first Google query this app was born.</p>
            <h4>Future work</h4>
            <p>Ranking students with similar interests based on measuring similarity in essay writing is just the beginning. I believe BetterTogether app can be improved in several fronts. We can collect data about personal traits, skill sets, study & work habits, etc, and show students who have same characteristics. Basically we could apply all NLP/AI/ML techniques that big online dating companies are using to match hundreds of millions of couples everyday to solve our problem: helping students navigate the class to find similar people to work in teams, fostering collaboration.<p>
        </div>
    </div>
    <div class="row">
        <div class="col-md-8 offset-md-2 col-xs-12 col-sm-10 offset-sm-1">
            <br/>
            <p class="lead text-center">
                <a role="button" class="btn btn-outline-primary btn-lg" href="javascript:history.back()">Go Back!</a>
                <a role="button" class="btn btn-outline-primary btn-lg" href="https://github.com/ucals/bettertogether/blob/master/tutorial.ipynb" target="_blank" rel="noopener noreferrer">Tutorial</a>
                <a role="button" class="btn btn-outline-primary btn-lg" href="https://goo.gl/forms/alQDVr3lmOUwvouE2" target="_blank" rel="noopener noreferrer">Feedback</a>
            </p>
            % include('credit.tpl')
        </div>
    </div>
</div>
% include('footer.tpl')