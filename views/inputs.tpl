% include('header.tpl')
<form method="POST" action="/plot">

<div class="container">
    <div class="row">
        <div class="col-md-8 offset-md-2 col-xs-12 col-sm-10 offset-sm-1">
            <h1 class="text-center">#bettertogether</h1>
            <br/>
            <p class="lead text-center">Select <strong>your name</strong> in the dropdown below:</p>
        </div>
    </div>
    <div class="row">
        <div class="col-md-8 offset-md-2 col-xs-12 col-sm-10 offset-sm-1">
            <p class="text-center">
                <select class="selectpicker increased" data-show-subtext="true" data-live-search="true" name="student">
                % for student in students:
                    <option value="{{student}}" {{"selected" if student =="Carlos Souza" else ""}}>{{student}}</option>
                % end
                </select>
            </p>
        </div>
    </div>
    <br/>
    <div class="row">
        <div class="col-md-8 offset-md-2 col-xs-12 col-sm-10 offset-sm-1 text-center">
            <p class="lead">Also select <strong>which assignment</strong> you want the NLP analysis to be based in:</p>
            <div class="radio">
                <label class="increased_radio">
                    <input type="radio" name="assignment" id="optionsRadios1" value="2">
                    Assignment 2: Exploring Educational Technology
                </label>
            </div>
            <div class="radio">
                <label class="increased_radio">
                    <input type="radio" name="assignment" id="optionsRadios2" value="3" checked>
                    Assignment 3: Exploring Your Areas
                </label>
            </div>
            <div class="radio">
                <label class="increased_radio">
                    <input type="radio" name="assignment" id="optionsRadios3" value="4">
                    Assignment 4: Exploring Your Problem
                </label>
            </div>
        </div>
    </div>
    <br/>
    <div class="row">
        <div class="col-md-8 offset-md-2 col-xs-12 col-sm-10 offset-sm-1">
            <p class="lead text-center"><input class="btn btn-primary btn-lg" type="submit" value="Find me similar students!"></p>
            % include('credit.tpl')
        </div>
    </div>
</div>

</form>
% include('footer.tpl')