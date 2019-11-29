pragma solidity ^0.4.2;

contract Election {
    // Model a Candidate
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
        string img;
    }

    // Store accounts that have voted
    mapping(address => bool) public voters;
    // Read/write candidates
    mapping(uint => Candidate) public candidates;
    // Store Candidates Count
    uint public candidatesCount;

    function Election () public {
        addCandidate("Lasanha", "http://www.receitasnestle.com.br/images/default-source/recipes/lasanha_a_bolonhesa_saborosa.jpg");
        addCandidate("Churrasco", "https://img.stpu.com.br/?img=https://s3.amazonaws.com/pu-mgr/default/a0R0f000010n3JWEAY/5cbdc891e4b04842fce04911.jpg&w=710&h=462");
    }

    function addCandidate (string _name, string _img) private {
        candidatesCount ++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0, _img);
    }

    function vote (uint _candidateId) public {
        // require that they haven't voted before
        //require(!voters[msg.sender]);

        // require a valid candidate
        require(_candidateId > 0 && _candidateId <= candidatesCount);

        // record that voter has voted
        voters[msg.sender] = true;

        // update candidate vote Count
        candidates[_candidateId].voteCount ++;
    }
}
