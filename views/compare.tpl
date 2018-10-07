% include('header_local.tpl')

<div class="container">
    <div class="row">
        <div class="col-md-8 offset-md-2 col-xs-12 col-sm-10 offset-sm-1">
            <h1 class="text-center">#bettertogether</h1>
            <br/>
            <p class="lead text-center"><strong>{{student_1}}</strong>, here's how your <strong>Assignment {{assignment}}</strong> compares with <strong>{{student_2}}</strong>'s:</p>
        </div>
    </div>
    <div class="row">
        <div class="col-md-8 offset-md-2 col-xs-12 col-sm-10 offset-sm-1">
            <div class="row">
                <div class="col-6">
                    <table class="table">
                        <thead>
                        <tr>
                            <th scope="col" style="width: 10%">#</th>
                            <th scope="col" style="width: 70%">{{student_1}}'s main topics:</th>
                            <th scope="col" style="width: 20%" class="text-center">Relevance score</th>
                        </tr>
                        </thead>
                        <tbody>
                        % for index, item in enumerate(entities_1):
                        <tr>
                            <th scope="row">{{index + 1}}</th>
                            <td>{{item.id}}</td>
                            <td class="text-center">{{"{0:.4f}".format(item.relevance_score)}}</td>
                        </tr>
                        % end
                        </tbody>
                    </table>
                </div>
                <div class="col-6">
                    <table class="table">
                        <thead>
                        <tr>
                            <th scope="col" style="width: 10%">#</th>
                            <th scope="col" style="width: 70%">{{student_2}}'s main topics:</th>
                            <th scope="col" style="width: 20%" class="text-center">Relevance score</th>
                        </tr>
                        </thead>
                        <tbody>
                        % for index, item in enumerate(entities_2):
                        <tr>
                            <th scope="row">{{index + 1}}</th>
                            <td>{{item.id}}</td>
                            <td class="text-center">{{"{0:.4f}".format(item.relevance_score)}}</td>
                        </tr>
                        % end
                        </tbody>
                    </table>

                </div>
            </div>
        </div>

    </div>
    <div class="row">
        <div class="col-md-8 offset-md-2 col-xs-12 col-sm-10 offset-sm-1">
            <p class="lead text-center">This uses <a href="https://www.textrazor.com/">TextRazor</a>'s API. Check <a href="#">the tutorial</a> to see how to it is used.</p>
            <br/>
            <p class="lead text-center">
                <a role="button" class="btn btn-outline-primary btn-lg" href="#">Go Back!</a>
                <a role="button" class="btn btn-outline-primary btn-lg" href="#">Tutorial</a>
                <a role="button" class="btn btn-outline-primary btn-lg" href="#">Feedback</a>
            </p>
            <p class="text-center">Created by <a href="mailto:souza@gatech.edu">Carlos Souza</a><p>
        </div>
    </div>
</div>

% include('footer.tpl')