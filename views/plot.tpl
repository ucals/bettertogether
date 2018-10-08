% include('header.tpl')
<div class="container">
    <div class="row">
        <div class="col-md-8 offset-md-2 col-xs-12 col-sm-10 offset-sm-1">
            <h1 class="text-center">#bettertogether</h1>
            <br/>
            <p class="lead text-center"><strong>{{student}}</strong>, based on <strong>Assignment {{assignment}}</strong>, these are the <strong>top 10</strong> similar students:</p>
        </div>
    </div>

    <div class="row">
        <div class="col-md-8 offset-md-2 col-xs-12 col-sm-10 offset-sm-1">

            <table class="table">
                <thead>
                <tr>
                    <th scope="col" style="width: 10%">#</th>
                    <th scope="col" style="width: 50%">Student</th>
                    <th scope="col" style="width: 30%" class="text-center">Similarity score</th>
                    <th scope="col" style="width: 10%"></th>
                </tr>
                </thead>
                <tbody>
                % for index, item in enumerate(similar_docs):
                <tr>
                    <th scope="row">{{index + 1}}</th>
                    <td>{{item[0]}}</td>
                    <td class="text-center">{{"{0:.4f}".format(item[1])}}</td>
                    <td class="text-center"><a  href="/compare/{{assignment}}/{{student}}/{{item[0]}}" role="button" class="btn btn-sm btn-primary"><span class="oi oi-magnifying-glass"></span></a></td>
                </tr>
                % end
                </tbody>
            </table>

        </div>
    </div>
    <div class="row">
        <div class="col-md-8 offset-md-2 col-xs-12 col-sm-10 offset-sm-1">
            <p class="lead text-center"><strong>Click on the  <span class="oi oi-magnifying-glass"></span>  button</strong> to see a comparison analysis of main topics.</p>
            <br/>
            <p class="lead text-center">
                <a role="button" class="btn btn-outline-primary btn-lg" href="/inputs">Start over!</a>
                <a role="button" class="btn btn-outline-primary btn-lg" href="/motivation">Motivation</a>
                <a role="button" class="btn btn-outline-primary btn-lg" href="https://github.com/ucals/bettertogether/blob/master/tutorial.ipynb" target="_blank" rel="noopener noreferrer">Tutorial</a>
                <a role="button" class="btn btn-outline-primary btn-lg" href="https://goo.gl/forms/alQDVr3lmOUwvouE2" target="_blank" rel="noopener noreferrer">Feedback</a>
            </p>
            <p class="text-center">Created by <a href="mailto:souza@gatech.edu">Carlos Souza</a><p>
        </div>
    </div>
</div>
% include('footer.tpl')